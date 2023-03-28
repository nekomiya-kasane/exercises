create view Q2 (course_id)
as
select course from (
	select distinct course from (
		select class_types.unswid as ctype, course, room
		from class_types, classes 
		where classes.ctype=class_types.id and class_types.unswid='LAB'
	) as t1
	group by course
	having count(room)-count(distinct room)=0
) as t2 left join courses on t2.course=courses.id 
left join semesters on semesters.id=courses.semester
left join subjects on subjects.id=courses.subject
where year=2011 and subjects.name ilike '%data%';