SELECT s.name as subject_name
FROM subjects s
JOIN grades g ON s.id = g.subject_id
JOIN students stu ON g.student_id = stu.id
JOIN teachers t ON s.teacher_id = t.id
WHERE stu.name = '<student_name>' AND t.name = '<teacher_name>';
