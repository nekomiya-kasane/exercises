select unswid as unsw_id, name from (
	select unswid, name, semester, count(distinct course) as course_cnt from people 
	inner join course_enrolments on course_enrolments.student=people.id
	left join courses on courses.id=course_enrolments.course
	where left(unswid::text, 1)::integer < 4
	group by semester, people.id
	order by unswid
) as t group by unsw_id, name
having max(course_cnt) > 1
;