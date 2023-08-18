import numpy as np
import matplotlib.pyplot as plt
from queue import Queue


def get_connected_components(img, threshold: int = 1, method: str = 'original', lattice: int = 4):

    assert (lattice == 4 or lattice == 9)

    if method == 'scipy':
        from scipy.ndimage import label
        labels, num_labels = label(img)  # type: ignore
        return labels
    elif method == 'opencv':
        import cv2
        num_labels, labels = cv2.connectedComponents(img)
        return labels

    labels = np.zeros_like(img, dtype=np.int16)

    label = 1
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if labels[i, j] == 0 and img[i, j] > 0:
                _dfs(img, labels, label, i, j, img[i, j], threshold, lattice)
                label += 1

    return labels, label - 1


def _dfs(image, labels, label, i, j, value, threshold, lattice):
    if i < 0 or i >= image.shape[0] or j < 0 or j >= image.shape[1] or labels[i, j] != 0:
        return

    if abs(image[i, j] - value) >= threshold:
        return

    labels[i, j] = label
    qu = Queue()
    qu.put((i, j))

    boundary = []

    def handle(_i, _j):
        if _i < 0 or _i >= image.shape[0] or _j < 0 or _j >= image.shape[1] or labels[_i, _j] != 0:
            return
        if abs(image[_i, _j] - value) >= threshold:
            boundary.append([_i, _j])
            labels[_i, _j] = -1
            return
        labels[_i, _j] = label
        qu.put((_i, _j))

    while qu._qsize():
        _i, _j = qu.get()
        handle(_i - 1, _j)
        handle(_i + 1, _j)
        handle(_i, _j - 1)
        handle(_i, _j + 1)
        if lattice == 9:
            handle(_i - 1, _j - 1)
            handle(_i + 1, _j + 1)
            handle(_i + 1, _j - 1)
            handle(_i - 1, _j + 1)

    for pt in boundary:
        labels[pt[0]][pt[1]] = 0


def plot_components(labels, label=[]):
    unique_values = set(np.unique(labels))
    colors = np.random.randint(0, 256, size=(len(unique_values), 3))

    colored = np.zeros((labels.shape[0], labels.shape[1], 3), dtype=np.uint8)

    for i, value in enumerate(unique_values):
        colored[labels == value] = colors[i] if value and (not len(label) or (i in label)) else np.array([0, 0, 0])

    plt.imshow(colored)

class ComponentInfo:
    corners = np.zeros((4, 2))
    major_axis = np.zeros((2, ))
    major_radius = 0
    minor_axis = np.zeros((2, ))
    minor_radius = 0
    center = np.zeros((2, ))
    size = 0.0
    cover = 0.0
    normalized = np.array([[]])

    def __str__(self) -> str:
        print("corners: ", self.corners)
        print("major_axis: ", self.major_axis)
        print("major_radius: ", self.major_radius)
        print("minor_axis: ", self.minor_axis)
        print("minor_radius: ", self.minor_radius)
        print("center: ", self.center)
        print("size: ", self.size)
        print("cover: ", self.cover)
        return ""
        


def get_components_info(labels, label, img=None):
    indices = np.argwhere(labels == label).astype(np.float32)
    center = np.array([np.mean(indices[:, 0]), np.mean(indices[:, 1])])
    indices[:, 0] -= center[0]
    indices[:, 1] -= center[1]

    cov_matrix = np.cov(indices.T)
    cov_matrix = np.nan_to_num(cov_matrix)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    min_eig_id, max_eig_id = np.argmin(eigenvalues), np.argmax(eigenvalues)
    min_eig_val, max_eig_val = np.sqrt(eigenvalues[min_eig_id]), np.sqrt(eigenvalues[max_eig_id])
    min_eig_vec, max_eig_vec = eigenvectors[:, min_eig_id], eigenvectors[:, max_eig_id]

    major, minor = center.copy(), center.copy()
    while labels[int(major[0]), int(major[1])]:
        major += max_eig_vec
    while labels[int(minor[0]), int(minor[1])]:
        minor += min_eig_vec
    
    major_axis = major - center + max_eig_vec
    minor_axis = minor - center + min_eig_vec

    info = ComponentInfo()
    info.center = center
    info.major_axis = major_axis
    info.minor_axis = minor_axis
    info.major_radius = int(np.linalg.norm(major_axis, 2))
    info.minor_radius = int(np.linalg.norm(minor_axis, 2))
    info.size = info.major_radius * info.minor_radius * 4
    info.cover = len(indices[:, 0]) / info.size if info.size > 0 else 0

    if img is None:
        return info
    
    info.normalized = np.zeros((info.minor_radius * 2 + 5, info.major_radius * 2 + 5))

    ang = np.arctan2(major_axis[0], major_axis[1])
    A = lambda t : np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

    for j in range(len(labels[0])):
        for i in range(len(labels)):
            if labels[i, j] != label:
                continue
            pos = np.array([float(j - center[1]), float(i - center[0])])
            coord = A(-ang) @ pos + np.array([info.major_radius, info.minor_radius])
            info.normalized[int(coord[1]), int(coord[0])] = img[i, j]

    return info

    







class Rect:
    bottom: int = 0
    top: int = 0
    left: int = 0
    right: int = 0

    width: int = 0
    height: int = 0

    def __init__(self, l=0, b=0, r=0, t=0):
        self.left, self.bottom, self.right, self.top = l, b, r, t

    def __str__(self) -> str:
        return f"Left: {self.left} Bottom: {self.bottom} Right: {self.right} Top: {self.top} Width: {self.width} Height: {self.height}"


def get_vertical_rect(corners):
    rect = Rect()

    rect.bottom = min([x[0] for x in corners])
    rect.top = max([x[0] for x in corners])
    rect.right = max([y[1] for y in corners])
    rect.left = min([y[1] for y in corners])

    rect.width = rect.right - rect.left
    rect.height = rect.top - rect.bottom

    return rect

def get_outer_box(labels, label):
    indices = np.where(labels == label)
    rect = Rect()

    rect.bottom = min(indices[1])
    rect.top = max(indices[1])
    rect.right = max(indices[0])
    rect.left = min(indices[0])

    rect.width = rect.right - rect.left
    rect.height = rect.bottom - rect.top

    return rect