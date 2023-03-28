-- COMP9311 23T1 Project Check
--
-- MyMyUNSW Check

SET client_min_messages TO WARNING;

create or replace function
	proj1_table_exists(tname text) returns boolean
as $$
declare
	_check integer := 0;
begin
	select count(*) into _check from pg_class
	where relname=tname and relkind='r';
	return (_check = 1);
end;
$$ language plpgsql;

create or replace function
	proj1_view_exists(tname text) returns boolean
as $$
declare
	_check integer := 0;
begin
	select count(*) into _check from pg_class
	where relname=tname and relkind='v';
	return (_check = 1);
end;
$$ language plpgsql;

create or replace function
	proj1_function_exists(tname text) returns boolean
as $$
declare
	_check integer := 0;
begin
	select count(*) into _check from pg_proc
	where proname=tname;
	return (_check > 0);
end;
$$ language plpgsql;

-- proj1_check_result:
-- * determines appropriate message, based on count of
--   excess and missing tuples in user output vs expected output

create or replace function
	proj1_check_result(_res text,nexcess integer, nmissing integer) returns text
as $$
begin
	if (nexcess = 0 and nmissing = 0) then
		return _res || ' correct';
	elsif (nexcess > 0 and nmissing = 0) then
		return _res || ' too many result tuples';
	elsif (nexcess = 0 and nmissing > 0) then
		return _res || ' missing result tuples';
	elsif (nexcess > 0 and nmissing > 0) then
		return _res || ' incorrect result tuples';
	end if;
end;
$$ language plpgsql;

-- proj1_check:
-- * compares output of user view/function against expected output
-- * returns string (text message) containing analysis of results

create or replace function
	proj1_check(_type text, _name text, _res text, _query text) returns text
as $$
declare
	nexcess integer;
	nmissing integer;
	excessQ text;
	missingQ text;
begin
	if (_type = 'view' and not proj1_view_exists(_name)) then
		return 'No '||_name||' view; did it load correctly?';
	elsif (_type = 'function' and not proj1_function_exists(_name)) then
		return 'No '||_name||' function; did it load correctly?';
	elsif (not proj1_table_exists(_res)) then
		return _res||': No expected results!';
	else
		excessQ := 'select count(*) '||
				 'from (('||_query||') except '||
				 '(select * from '||_res||')) as X';
		-- raise notice 'Q: %',excessQ;
		execute excessQ into nexcess;
		missingQ := 'select count(*) '||
					'from ((select * from '||_res||') '||
					'except ('||_query||')) as X';
		-- raise notice 'Q: %',missingQ;
		execute missingQ into nmissing;
		return proj1_check_result(_res,nexcess,nmissing);
	end if;
	return '???';
end;
$$ language plpgsql;

-- proj1_rescheck:
-- * compares output of user function against expected result
-- * returns string (text message) containing analysis of results

create or replace function
	proj1_rescheck(_type text, _name text, _res text, _query text) returns text
as $$
declare
	_sql text;
	_chk boolean;
begin
	if (_type = 'function' and not proj1_function_exists(_name)) then
		return 'No '||_name||' function; did it load correctly?';
	elsif (_res is null) then
		_sql := 'select ('||_query||') is null';
		-- raise notice 'SQL: %',_sql;
		execute _sql into _chk;
		-- raise notice 'CHK: %',_chk;
	else
		_sql := 'select ('||_query||') = '||quote_literal(_res);
		-- raise notice 'SQL: %',_sql;
		execute _sql into _chk;
		-- raise notice 'CHK: %',_chk;
	end if;
	if (_chk) then
		return 'correct';
	else
		return 'incorrect result';
	end if;
end;
$$ language plpgsql;

-- check_all:
-- * run all of the checks and return a table of results

drop type if exists TestingResult cascade;
create type TestingResult as (test text, result text);

create or replace function
	check_all() returns setof TestingResult
as $$
declare
	i int;
	testQ text;
	result text;
	out TestingResult;
	tests text[] := array['q1', 'q2', 'q3', 'q4', 'q5','q6','q7','q8',
	'q9a','q9b','q9c','q9d','q9e',
	'q10a','q10b','q10c','q10d','q10e'];
begin
	for i in array_lower(tests,1) .. array_upper(tests,1)
	loop
		testQ := 'select check_'||tests[i]||'()';
		execute testQ into result;
		out := (tests[i],result);
		return next out;
	end loop;
	return;
end;
$$ language plpgsql;


--
-- Check functions for specific test-cases in Project 1
--

create or replace function check_q1() returns text
as $chk$
select proj1_check('view','q1','q1_expected',
									 $$select * from q1$$)
$chk$ language sql;

create or replace function check_q2() returns text
as $chk$
select proj1_check('view','q2','q2_expected',
									 $$select * from q2$$)
$chk$ language sql;

create or replace function check_q3() returns text
as $chk$
select proj1_check('view','q3','q3_expected',
									 $$select * from q3$$)
$chk$ language sql;

create or replace function check_q4() returns text
as $chk$
select proj1_check('view','q4','q4_expected',
									 $$select * from q4$$)
$chk$ language sql;

create or replace function check_q5() returns text
as $chk$
select proj1_check('view','q5','q5_expected',
									 $$select * from q5$$)
$chk$ language sql;

create or replace function check_q6() returns text
as $chk$
select proj1_check('view','q6','q6_expected',
									 $$select * from q6$$)
$chk$ language sql;

create or replace function check_q7() returns text
as $chk$
select proj1_check('view','q7','q7_expected',
									 $$select * from q7$$)
$chk$ language sql;

create or replace function check_q8() returns text
as $chk$
select proj1_check('view','q8','q8_expected',
									 $$select * from q8$$)
$chk$ language sql;


-- Q9
create or replace function check_q9a() returns text
as $chk$
select proj1_check('function','q9','q9a_expected',
									 $$select q9(3011590)$$)
$chk$ language sql;

create or replace function check_q9b() returns text
as $chk$
select proj1_check('function','q9','q9b_expected',
									 $$select q9(3101318)$$)
$chk$ language sql;

create or replace function check_q9c() returns text
as $chk$
select proj1_check('function','q9','q9c_expected',
									 $$select q9(3108164)$$)
$chk$ language sql;

create or replace function check_q9d() returns text
as $chk$
select proj1_check('function','q9','q9d_expected',
									 $$select q9(3300395)$$)
$chk$ language sql;

create or replace function check_q9e() returns text
as $chk$
select proj1_check('function','q9','q9e_expected',
									 $$select q9(3463281)$$)
$chk$ language sql;

-- Q10 
create or replace function check_q10a() returns text
as $chk$
select proj1_check('function','q10','q10a_expected',
									 $$select q10(2012, 'S1', 89)$$)
$chk$ language sql;

create or replace function check_q10b() returns text
as $chk$
select proj1_check('function','q10','q10b_expected',
									 $$select q10(2008, 'S2', 64)$$)
$chk$ language sql;

create or replace function check_q10c() returns text
as $chk$
select proj1_check('function','q10','q10c_expected',
									 $$select q10(2010, 'S1', 31)$$)
$chk$ language sql;

create or replace function check_q10d() returns text
as $chk$
select proj1_check('function','q10','q10d_expected',
									 $$select q10(2010, 'S2', 17)$$)
$chk$ language sql;

create or replace function check_q10e() returns text
as $chk$
select proj1_check('function','q10','q10e_expected',
									 $$select q10(2009, 'S2', 75)$$)
$chk$ language sql;

--
-- Tables of expected results for test cases
--

drop table if exists q1_expected;
create table q1_expected (
	subject_code character(8)
);

drop table if exists q2_expected;
create table q2_expected (
	course_id integer
);

drop table if exists q3_expected;
create table q3_expected (
	unsw_id integer, name longname
);

drop table if exists q4_expected;
create table q4_expected (
	unsw_id integer, program integer
);

drop table if exists q5_expected;
create table q5_expected (
	unsw_id integer, program integer, course integer
);

drop table if exists q6_expected;
create table q6_expected (
	school_id integer, building_count integer
);

drop table if exists q7_expected;
create table q7_expected (
	course_id integer, staff_name longname
);

drop table if exists q8_expected;
create table q8_expected (
	unsw_id integer, name longname
);

drop table if exists q9a_expected;
create table q9a_expected (
	q9 text
);

drop table if exists q9b_expected;
create table q9b_expected (
	q9 text
);

drop table if exists q9c_expected;
create table q9c_expected (
	q9 text
);

drop table if exists q9d_expected;
create table q9d_expected (
	q9 text
);

drop table if exists q9e_expected;
create table q9e_expected (
	q9 text
);



drop table if exists q10a_expected;
create table q10a_expected (
	q10 text
);

drop table if exists q10b_expected;
create table q10b_expected (
	q10 text
);

drop table if exists q10c_expected;
create table q10c_expected (
	q10 text
);

drop table if exists q10d_expected;
create table q10d_expected (
	q10 text
);

drop table if exists q10e_expected;
create table q10e_expected (
	q10 text
);


-- ( )+\|+( )+

COPY q1_expected (subject_code) FROM stdin;
INFS2848
INFS5848
\.

COPY q2_expected (course_id) FROM stdin;
54681
58034
59078
\.


COPY q3_expected (unsw_id, name) FROM stdin;
3210020	Laura Wen
3210039	Hygeia Tupaz
3210072	Molly Ngan
3210128	Caine Cotton
3210132	Benjamin Saker
3210136	Nicholas Paipetis
3210149	Carol Froggatt
3210150	Anton Stapley
3210155	Bee Loo
3210166	Quang Randall
3210199	Si Hua
3210209	Hal Wehr
3210231	Mun Tong
3210341	Rania Matkovich
3210342	Vivilia Nuraeni
3210354	Kate Venezia
3210366	Stevan Broadsmith
3210387	Yuxing Yamato
3210389	Chi Tjin
3210404	Tully Pongracic
3210410	Hayley McGahey
3210415	Shaun Kuy
3210428	Lucas Suradi
3210439	Emma Ratsep
3210450	Tzen Phua
3210453	Brendon Renton
3210479	Melinda Huleatt
3210519	Christina Edelstein
3210561	N Montolalu
3210563	Michael Eddy
3210564	Cathryn Barsi
3210613	Aran Paice
3210646	Taylor Shen
3210684	Jannene Mc Keown
3210692	Mick Sheen
3210701	Erin Farfan
3210709	Michael Marquart
3210744	Yvette Dinhvu
3210751	Hon Qian
3210765	Wee Zhang
3210775	Raji O'Brien
3210782	Peter Dibianco
3210808	Philip Chua
3210818	Angela Kung
3210827	Bryce Macpherson
3210872	Russell Blackwell
3210894	Ya Chitdamrong
3210908	Kendal Heald
3210934	Benjamin Wang
3210945	Stina Nielsen
3210951	Natan Utjesenovic
\.



COPY q4_expected (unsw_id, program) FROM stdin;
3106182	819
8168934	1075
3283054	1044
3087372	586
\.

COPY q5_expected (unsw_id, program, course) FROM stdin;
3000010	588	15407
3014244	638	16269
3036537	698	16108
3036537	698	18225
3050506	533	17371
3065280	737	14099
3092300	663	16571
3100308	629	15149
3105004	635	17708
3107994	698	16092
3114933	1256	16358
3120361	819	14398
3123898	629	15140
3130832	696	16076
3139182	750	15073
3146249	508	15668
3151363	698	16020
3155759	500	17113
3158724	839	18227
3158724	839	18270
3168798	603	16258
3170224	616	17605
3171162	697	18261
3185371	533	13944
3191123	534	16630
3192103	804	16844
\.

COPY q6_expected (school_id, building_count) FROM stdin;
4	22
17	16
30	22
49	21
69	23
71	16
75	23
89	20
102	22
103	19
106	20
113	21
147	25
152	15
174	21
176	18
180	17
197	20
238	22
240	22
703	17
1134	18
1342	19
1613	20
\.


COPY q7_expected (course_id, staff_name) FROM stdin;
68806	Saretta Lee
70151	Yueping Alex Wang
\.


COPY q8_expected (unsw_id, name) FROM stdin;
3144795	Salma Lambie
3188799	Lauren Shoebridge
\.


COPY q9a_expected (q9) FROM stdin;
26878 3120769 2261
30064 3021026 2415
30064 9407594 2415
30069 3152149 2415
30069 7246841 2415
\.


COPY q9b_expected (q9) FROM stdin;
40885 8499696 2982
40885 3293919 2982
40885 3201776 2982
51243 8499696 3486
51244 3120769 3486
51244 3355911 3486
51250 3021026 3486
51250 3245976 3486
51250 3203981 3486
51256 3203519 3486
51256 2169617 3486
51256 7246841 3486
\.


COPY q9c_expected (q9) FROM stdin;
41654 9155962 2982
41654 3191415 2982
41654 2252032 2982
41654 3031001 2982
41655 3065011 2982
52112 3005065 3486
52112 3260150 3486
52112 3269717 3486
52112 3027173 3486
55803 3269895 3710
\.


COPY q9d_expected (q9) FROM stdin;
47277 3084028 3346
50502 3171293 3486
50502 3242608 3486
50502 3039168 3486
50502 3030995 3486
50502 3262096 3486
50560 3084028 3486
54286 3039168 3710
54286 3307288 3710
57414 9160956 3850
57414 3391991 3850
57461 3030995 3850
57461 3307288 3850
\.

COPY q9e_expected (q9) FROM stdin;
61195 3308996 4074
64376 3071338 4221
64376 3308996 4221
64376 3426857 4221
64379 9160956 4221
\.


COPY q10a_expected (q10) FROM stdin;
3201489 92.67
3209070 91.25
3209249 86.00
3219354 87.00
3231195 93.00
3243180 89.67
3250411 91.75
3268800 88.00
3301777 90.00
3319767 89.75
3323247 92.00
3329009 94.75
3331317 92.00
3331709 88.25
3334567 89.25
3345244 85.67
3348443 89.00
3350897 85.25
3356955 87.50
3366939 90.00
3372020 89.00
3372638 86.00
3373112 85.50
3378028 94.00
3378141 95.50
3386050 85.67
3391524 90.00
3395758 90.00
3397891 88.00
3436823 93.50
3486952 86.25
3493871 87.25
\.


COPY q10b_expected (q10) FROM stdin;
3102979 85.33
3107792 85.50
3109384 87.50
3154588 95.00
3203674 89.00
3221183 89.00
3224014 93.50
3227219 87.00
3240514 91.50
3278558 86.00
3287860 92.00
3289314 87.00
3293180 89.00
\.


COPY q10c_expected (q10) FROM stdin;
3148060 86.00
3155213 88.00
3203226 87.00
3204088 85.67
3210773 85.50
3216371 87.00
3219005 88.00
3221756 85.33
3226730 99.00
3235115 88.00
3236758 86.33
3241111 88.00
3244509 85.50
3252113 87.50
3254114 86.25
3255086 87.00
3262781 87.00
3266768 86.00
3267438 91.25
3268015 86.00
3269044 94.00
3274060 87.00
3277012 90.50
3279765 88.00
3287427 85.25
3296439 86.00
3348178 85.50
3359392 87.00
3361707 89.75
3364669 85.25
3385226 89.00
3385989 87.00
3390325 87.50
\.


COPY q10d_expected (q10) FROM stdin;
1096066 86.50
3270610 86.00
3281096 86.00
\.

COPY q10e_expected (q10) FROM stdin;
3230522 88.50
3301140 89.50
\.
