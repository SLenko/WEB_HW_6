SELECT t.name as lector_name, s.name as subject_name
FROM lectors t
JOIN subjects s ON t.id = s.lector_id
WHERE t.id = 2;