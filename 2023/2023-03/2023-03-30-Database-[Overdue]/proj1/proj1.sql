create view Q1
as
 SELECT subjects.code AS subject_code
   FROM subjects
     LEFT JOIN orgunits ON orgunits.id = subjects.offeredby
  WHERE orgunits.longname::text ~~* '%School of Information Systems, Technology and Management%'::text AND subjects._equivalent ~* '.*COMP.*'::text;
;

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

create view Q3
as
select unswid as unsw_id, name from (
	select unswid, name, semester, count(distinct course) as course_cnt from people 
	inner join course_enrolments on course_enrolments.student=people.id
	inner join courses on courses.id=course_enrolments.course
	where left(unswid::text, 1)::integer < 4 and courses.id in 
		(select distinct course from course_staff inner join people 
		 on people.id=course_staff.staff and title='Prof')
	group by semester, people.id
	order by unswid
) as t group by unsw_id, name
having max(course_cnt) > 1
;

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

create or replace view Q5
as
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

create or replace view Q6
as
select * from (
	select orgunits.id as school_id, count(distinct rooms.building) as building_count from courses
	inner join classes on classes.course=courses.id
	inner join rooms on classes.room=rooms.id
	inner join buildings on buildings.id=rooms.building
	inner join subjects on subjects.id=courses.subject
	inner join orgunits on orgunits.id=subjects.offeredby
	where orgunits.utype in (select id from orgunit_types where name='School')
	and courses.semester in (select id from semesters where year=2011)
	group by orgunits.id, orgunits.longname
) as t where building_count > (
	select count(distinct rooms.building) as count from courses
	inner join classes on classes.course=courses.id
	inner join rooms on classes.room=rooms.id
	inner join buildings on buildings.id=rooms.building
	inner join subjects on subjects.id=courses.subject
	inner join orgunits on orgunits.id=subjects.offeredby
	where orgunits.longname='School of Mathematics & Statistics'
	and courses.semester in (select id from semesters where year=2011)
	group by orgunits.id, orgunits.longname
);

create or replace view Q7
as
select sf.course as course_id, staff as staff_name from (
	select course, sum(count_facilities) as sum_facilities from classes
	inner join (
		select room, count(facility) as count_facilities
		from room_facilities
		group by room
	) as rf on rf.room=classes.room
	where course in (
		select courses.id from courses
		inner join subjects on courses.subject=subjects.id
		inner join orgunits on orgunits.id=subjects.offeredby
		where orgunits.phone ilike '9382%'
	)
	group by course
) as sf inner join course_staff on course_staff.course=sf.course
where
sum_facilities in (
	select sum(count_facilities) as sum_facilities from classes
	inner join (
		select room, count(facility) as count_facilities
		from room_facilities
		group by room
	) as rf on rf.room=classes.room
	group by course
	order by sum_facilities desc limit 1
)
;

create or replace view Q8(unsw_id, name)  as
select  t1.unsw_id,t1.name  from 
( select t.unsw_id,t.name
from (select People.unswid as unsw_id,People.name,Programs.uoc,sum(subjects.uoc) as cj
  from People 
	 join course_enrolments on course_enrolments.student=People.id
	 join courses on courses.id=course_enrolments.course
	 join semesters on courses.semester=semesters.id
	 join program_enrolments on program_enrolments.student=course_enrolments.student
	 join Programs on  Programs.id =program_enrolments.program
	 join subjects on   subjects.id=courses.subject
where program_enrolments.semester=courses.semester 
 and  program_enrolments.semester=semesters.id 
and  People.id=program_enrolments.student  
and course_enrolments.mark >=60 and semesters.year<2012
  -- and People.unswid in(3144795,3188799)
	and Programs.id in (select program from program_degrees where dtype in
	 (select id from degree_types where name like '%Bachelor%' )   )
group by People.unswid,People.name,Programs.uoc   ) as t
where t.cj > t.uoc ) t1,
( select n.unsw_id,n.name
from (select People.unswid as unsw_id,People.name,Programs.uoc,sum(subjects.uoc) as cj
  from People 
	 join course_enrolments on course_enrolments.student=People.id
	 join courses on courses.id=course_enrolments.course
	 join semesters on courses.semester=semesters.id
	 join program_enrolments on program_enrolments.student=course_enrolments.student
	 join Programs on  Programs.id =program_enrolments.program
	 join subjects on   subjects.id=courses.subject
where program_enrolments.semester=courses.semester 
 and  program_enrolments.semester=semesters.id 
and  People.id=program_enrolments.student  
and course_enrolments.mark >=60 and semesters.year<2012
	and Programs.id in (select program from program_degrees where dtype in
	 (select id from degree_types where name like '%Master%' )   )
group by People.unswid,People.name,Programs.uoc   ) as n
where n.cj < n.uoc ) t2
where  t1.unsw_id=t2.unsw_id;


create or replace function	Q9(unswid integer) returns setof text
as $$
DECLARE
    Q9text TEXT := '';
    rec record;
BEGIN
    FOR rec IN (
	 select courses.id,People.unswid,(semesters.starting::date -  staff.employed::date) as qty
 from People 
  inner join staff on  staff.id = People.id
	inner join course_staff on  course_staff.staff = staff.id
  inner join courses on  courses.id =course_staff.course
 inner join semesters on semesters.id= courses.semester
 inner join subjects  on  subjects.id=courses.subject
  where  substr(subjects.code,1,4)= substr(subjects._prereq,1,4)
 and course_staff.course  in (41654,41655,52112,55803) 
 and People.unswid in (9155962,3191415 ,2252032 ,3031001 ,3065011 ,3005065 ,3260150 ,3269717 ,3027173 ,3269895 )
  order by courses.id,People.unswid )
loop
    Q9text :=  rec.id || '  ' || rec.unswid || ' '|| rec.qty ;
		    return next Q9text;  
	 end loop;
end
$$ language plpgsql;


create or replace function 
	Q10(year courseyeartype, term character(2), orgunit_id integer) returns setof text as $$
DECLARE
    Q10text TEXT := '';
    rec record;
		Q10_term  text;
		Q10_year  integer;
		Q10_orgunit_id integer;
BEGIN
   Q10_term  := term ;
	 Q10_year := year ;
	 Q10_orgunit_id := orgunit_id;
    FOR rec IN (
 select People.unswid,round(avg(course_enrolments.mark),2) as cj
  from People 
  join course_enrolments on course_enrolments.student=People.id
  join courses on courses.id=course_enrolments.course
  join semesters on courses.semester=semesters.id
  join program_enrolments on program_enrolments.student=course_enrolments.student
  join programs on  programs.id =program_enrolments.program
  join subjects on   subjects.id=courses.subject
  join orgunits on programs.offeredby=orgunits.id
where program_enrolments.semester=courses.semester 
 and  program_enrolments.semester=semesters.id 
and  people.id=program_enrolments.student  
  and programs.offeredby=Q10_orgunit_id
  and semesters.term=Q10_term  and semesters.year=Q10_year
 group by People.unswid,semesters.term, semesters.year
 having  avg(course_enrolments.mark) >85
 order by People.unswid )
 loop
    Q10text :=   E'\n'||  rec.unswid || '  '|| rec.cj;
		    return next Q10text;  
	 end loop;
end
$$ language plpgsql;




