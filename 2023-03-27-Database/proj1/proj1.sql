-- comp9311 23T1 Project 1

-- Q1:
create or replace view Q1(subject_code)
as
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q2:
create or replace view Q2(course_id)
as
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q3:
create or replace view Q3(unsw_id, name)
as
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q4:
create or replace view Q4(unsw_id, program)
as
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q5:
create or replace view Q5(unsw_id, program, course)
as
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q6:
create or replace view Q6(school_id, building_count)
as
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q7:
create or replace view Q7(course_id, staff_name)
as
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q8:
create or replace view Q8(unsw_id, name)
as
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q9:
create or replace function 
	Q9(unswid integer) returns setof text
as $$
--... SQL statements, possibly using other views/functions defined by you ...
$$ language plpgsql;

-- Q10
create or replace function 
	Q10(year courseyeartype, term character(2), orgunit_id integer) returns setof text
as $$
--... SQL statements, possibly using other views/functions defined by you ...
$$ language plpgsql;
