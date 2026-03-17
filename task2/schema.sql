-- =========================
-- CUSTOMERS TABLE
-- =========================
CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- AGENTS TABLE
-- =========================
CREATE TABLE agents (
    agent_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- TICKETS TABLE
-- =========================
CREATE TABLE tickets (
    ticket_id SERIAL PRIMARY KEY,
    customer_id VARCHAR(50),
    agent_id VARCHAR(50),
    status VARCHAR(20) DEFAULT 'open',
    priority VARCHAR(20) DEFAULT 'normal',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

-- =========================
-- MESSAGES TABLE
-- =========================
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    ticket_id INTEGER,
    sender_type VARCHAR(20),
    message_text TEXT,
    channel VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id)
);

-- =========================
-- INDEXES (Performance)
-- =========================
CREATE INDEX idx_ticket_customer ON tickets(customer_id);
CREATE INDEX idx_messages_ticket ON messages(ticket_id);

-- =========================
-- SAMPLE DATA
-- =========================

INSERT INTO customers (customer_id, name, email, phone)
VALUES ('cust_101', 'Varun', 'varun@email.com', '9999999999');

INSERT INTO agents (agent_id, name, email)
VALUES ('agent_1', 'Support Agent', 'agent@email.com');

INSERT INTO tickets (customer_id, agent_id, status, priority)
VALUES ('cust_101', 'agent_1', 'open', 'high');

INSERT INTO messages (ticket_id, sender_type, message_text, channel)
VALUES (1, 'customer', 'My internet is not working', 'chat');