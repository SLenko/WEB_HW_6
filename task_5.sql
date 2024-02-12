SELECT t.name as teacher_name, s.name as subject_name
FROM teachers t
JOIN subjects s ON t.id = s.teacher_id
WHERE t.id = <teacher_id>;
