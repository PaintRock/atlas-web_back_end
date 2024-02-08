-- Create an index on table names
CREATE INDEX idx_name_first_score ON names ON (name(1), score);
