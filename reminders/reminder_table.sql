CREATE TABLE reminders(
    reminder_id INT AUTO_INCREMENT ,
    remind_for TEXT,
    reminder_time_hours INT,
    reminder_time_minutes INT,
    reminder_time_am_or_pm VARCHAR(2),
    reminder_status VARCHAR(25),
    CONSTRAINT PK_reminders PRIMARY KEY (reminder_id)
    );

