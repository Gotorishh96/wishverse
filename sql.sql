CREATE DATABASE wishverse;
USE wishverse;

CREATE TABLE photos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    img_url VARCHAR(255),
    caption TEXT
);

CREATE TABLE timeline_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_date DATE,
    title VARCHAR(100),
    description TEXT
);
INSERT INTO photos (img_url, caption)
VALUES 
('images/photo1.jpg', 'Our first picture ❤️'),
('images/photo2.jpg', 'A beautiful memory 💫');

INSERT INTO timeline_events (event_date, title, description)
VALUES 
('2023-10-16', 'First Meeting', 'The day we first met.'),
('2024-12-06', 'Our First Trip', 'Adventure and laughter!');
