-- index on names and score
CREATE INDEX idx_name_first_score ON names (LEFT (name, (1), score);