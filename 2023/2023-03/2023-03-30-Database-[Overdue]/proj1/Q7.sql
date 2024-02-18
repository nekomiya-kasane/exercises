
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