CREATE TABLE toxigen_data (
    id SERIAL PRIMARY KEY,
    prompt TEXT,
    generation TEXT,
    generation_method VARCHAR(50),
    group_label VARCHAR(50),
    prompt_label INTEGER,
    roberta_prediction FLOAT
);
