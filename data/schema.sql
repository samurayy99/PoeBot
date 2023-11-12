-- schema.sql

-- Enable foreign key constraint
PRAGMA foreign_keys = ON;

-- Create Conversations table
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_time TEXT NOT NULL,
    end_time TEXT,
    status TEXT NOT NULL CHECK(status IN ('Active', 'Closed', 'Pending'))
);

-- Create Messages table
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id INTEGER NOT NULL,
    timestamp TEXT NOT NULL,
    message_text TEXT NOT NULL,
    sender_type TEXT NOT NULL CHECK(sender_type IN ('User', 'Bot')),
    media_type TEXT, -- To store the type of media if any message includes media
    file_reference INTEGER, -- To reference any file attached to the message
    context TEXT, -- To store the context or intent of the message
    FOREIGN KEY (conversation_id) REFERENCES conversations (id) ON DELETE CASCADE,
    FOREIGN KEY (file_reference) REFERENCES files (id) ON DELETE SET NULL
);

-- Create Tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    due_date TEXT,
    status TEXT NOT NULL CHECK(status IN ('Pending', 'Completed', 'Overdue')),
    priority INTEGER CHECK(priority BETWEEN 1 AND 5), -- 1 for highest priority
    category TEXT -- To categorize the task for filtering
);

-- Create Files table
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    upload_time TEXT NOT NULL,
    size INTEGER NOT NULL,
    type TEXT NOT NULL -- To categorize the file type for filtering
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_messages_conversation_id ON messages (conversation_id);
CREATE INDEX IF NOT EXISTS idx_tasks_priority ON tasks (priority);
CREATE INDEX IF NOT EXISTS idx_files_type ON files (type);
