-- PRAGMA foreign_keys = ON; - activate Foreign Key support ...
--- needs to run every time
-- so ON DELETE CASCADE works on junction tables like "student_lessons".

CREATE TABLE students(
student_id INTEGER PRIMARY KEY,
name NOT NULL
);

CREATE TABLE teachers(
teacher_id INTEGER PRIMARY KEY,
name NOT NULL
);

CREATE TABLE instruments(
instrument_id INTEGER PRIMARY KEY,
name NOT NULL UNIQUE
);



CREATE TABLE lessons(
lesson_id INTEGER PRIMARY KEY,
lesson_date TEXT NOT NULL,
start_time  TEXT NOT NULL,
room TEXT NOT NULL,
teacher_id INTEGER,
instrument_id INTEGER,
FOREIGN Key (teacher_id) REFERENCES teachers (teacher_id),
FOREIGN KEY (instrument_id) REFERENCES instruments (instrument_id)
);

CREATE TABLE student_lesson(
student_id INTEGER,
lesson_id INTEGER,
PRIMARY KEY (student_id, lesson_id),
FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id) ON DELETE CASCADE
);
 
CREATE TABLE teacher_instrument(
teacher_id INTEGER,
instrument_id INTEGER,
FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);



