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