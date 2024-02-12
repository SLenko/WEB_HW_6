SELECT t.name as teacher_name, AVG(g.grade) as avg_grade
FROM teachers t
JOIN subjects s ON t.id = s.teacher_id
JOIN grades g ON s.id = g.subject_id
WHERE t.id = <teacher_id>
GROUP BY t.id;
