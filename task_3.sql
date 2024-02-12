SELECT g.name, AVG(gg.grade) as avg_grade
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN grades gg ON s.id = gg.student_id
WHERE gg.subject_id = 4
GROUP BY g.id;
