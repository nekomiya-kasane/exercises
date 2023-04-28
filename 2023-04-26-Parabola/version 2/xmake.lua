set_project("DaijinTheNeko")

add_rules("mode.debug", "mode.release")

set_languages("c99", "c++17")

if is_plat("windows") then
    add_cxflags("-MT")
    add_defines("_CRT_SECURE_NO_WARNINGS")
    add_shflags("-nodefaultlib:msvcrt.lib")
    add_links("kernel32", "user32", "gdi32", "advapi32", "shell32")
end

-- EasyX
package("easyx")
    set_description("easyx")
    
    on_load(function (package)
        package:set("installdir", path.join(os.scriptdir(), package:plat(), package:arch(), package:mode()))
    end)

    on_fetch(function (package) 
        local result = {}
        result.links = "EasyXa"
        result.linkdirs = package:installdir("lib")
        result.includedirs = package:installdir("include")
        return result
    end)
package_end()

-- Main Project: DaijinTheNeko
target("DaijinTheNeko")
    set_kind("binary")
    add_files("src/*.cpp")

    add_packages("easyx")
    add_linkdirs("easyx/lib") -- ??
    -- add_ldflags("/MDd")
target_end()


