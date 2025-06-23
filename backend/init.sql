-- Initialize the employees table
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL
);

-- Insert some sample data
INSERT INTO employees (name, role) VALUES
    ('John Doe', 'Software Engineer'),
    ('Jane Smith', 'Product Manager'),
    ('Bob Johnson', 'DevOps Engineer')
ON CONFLICT DO NOTHING;
