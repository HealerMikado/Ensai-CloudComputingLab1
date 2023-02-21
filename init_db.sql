CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT 
    , description text
    , "user" text
);

INSERT INTO task (description, "user") VALUES
('Préparer le cours', 'Rémi'),
('Ajouter des gif', 'Rémi'),
('Donner le cours', 'Rémi'),
('???', 'Rémi');
