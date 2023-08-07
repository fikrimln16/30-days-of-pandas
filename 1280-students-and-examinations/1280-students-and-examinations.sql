# Write your MySQL query statement below

SELECT st.student_id, st.student_name, su.subject_name, count(ex.subject_name) as attended_exams
FROM Students st
JOIN Subjects su 
LEFT JOIN Examinations ex
ON ex.student_id = st.student_id
AND ex.subject_name = su.subject_name
GROUP BY st.student_id, su.subject_name
ORDER BY st.student_id
