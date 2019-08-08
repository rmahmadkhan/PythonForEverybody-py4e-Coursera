The file in the folder named "roste_data.json" is the file given to each student of the course differntly.

If you are taking the course, you may put the file given to you and then open sqlite file in sql browser.
Then enter the following command to get the desired output of assignemnet:

SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
