create view Q4 (unsw_id, program)
as
select unswid, program from (
	select student, program, count(distinct stream_enrolments) as cnt
	from program_enrolments 
	left join stream_enrolments on program_enrolments.id=stream_enrolments.partof
	left join stream_types on stream_types.id=stream_enrolments.stream
	where stream_types.description @@ to_tsquery('Major | Research')
	group by student, program
	order by student
) as t 
left join people on people.id=t.student
group by student, unswid, program
having max(t.cnt) >= 2
;