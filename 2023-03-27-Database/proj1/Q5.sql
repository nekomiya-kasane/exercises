select unswid as unsw_id, course, program from (
	select program_enrolments.student as student, course, program from course_enrolments 
	left join courses on courses.id=course_enrolments.course
	left join subjects on subjects.id=courses.subject
	inner join program_enrolments on program_enrolments.student=course_enrolments.student
	left join programs on programs.id=program_enrolments.program
	where course in (select course from course_enrolments group by course having max(course_enrolments.mark)>=98)
	and program_enrolments.semester in (select id from semesters where year=2005)
	and courses.semester in (select id from semesters where year=2005)
	and subjects.offeredby<>programs.offeredby
) as t1 left join people on people.id=t1.student
;