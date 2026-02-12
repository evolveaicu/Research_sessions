import { useState, useEffect } from 'react'
import './App.css'

const API_URL = 'http://localhost:8000/api'

function App() {
  const [tasks, setTasks] = useState([])
  const [title, setTitle] = useState('')
  const [priority, setPriority] = useState('3')
  const [error, setError] = useState('')

  // Fetch tasks when component loads
  useEffect(() => {
    fetchTasks()
  }, [])

  const fetchTasks = async () => {
    try {
      const response = await fetch(`${API_URL}/tasks`)
      const data = await response.json()
      setTasks(data)
    } catch (err) {
      setError('Failed to load tasks')
    }
  }

  const createTask = async (e) => {
    e.preventDefault()
    setError('')

    try {
      const response = await fetch(`${API_URL}/tasks`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title: title,
          priority: parseInt(priority)  // Convert string to number!
        })
      })

      if (!response.ok) {
        const error = await response.json()
        setError(error.detail[0]?.msg || 'Failed to create task')
        return
      }

      const newTask = await response.json()
      setTasks([...tasks, newTask])
      setTitle('')
      setPriority('3')
    } catch (err) {
      setError('Network error')
    }
  }

  const toggleTask = async (taskId, currentStatus) => {
    try {
      const response = await fetch(`${API_URL}/tasks/${taskId}?completed=${!currentStatus}`, {
        method: 'PATCH'
      })

      const updatedTask = await response.json()
      setTasks(tasks.map(t => t.id === taskId ? updatedTask : t))
    } catch (err) {
      setError('Failed to update task')
    }
  }

  const deleteTask = async (taskId) => {
    try {
      await fetch(`${API_URL}/tasks/${taskId}`, {
        method: 'DELETE'
      })

      setTasks(tasks.filter(t => t.id !== taskId))
    } catch (err) {
      setError('Failed to delete task')
    }
  }

  return (
    <div className="app">
      <header>
        <h1>Task Manager</h1>
        <p>React + FastAPI</p>
      </header>

      <div className="container">
        {/* Create Task Form */}
        <form onSubmit={createTask} className="task-form">
          <h2>Add Task</h2>

          {error && <div className="error">{error}</div>}

          <input
            type="text"
            placeholder="Task title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />

          <select value={priority} onChange={(e) => setPriority(e.target.value)}>
            <option value="1">Low Priority</option>
            <option value="2">Medium-Low</option>
            <option value="3">Medium</option>
            <option value="4">Medium-High</option>
            <option value="5">High Priority</option>
          </select>

          <button type="submit">Add Task</button>
        </form>

        {/* Task List */}
        <div className="task-list">
          <h2>Tasks ({tasks.length})</h2>

          {tasks.length === 0 ? (
            <p className="empty">No tasks yet</p>
          ) : (
            tasks.map(task => (
              <div key={task.id} className={`task priority-${task.priority}`}>
                <div className="task-content">
                  <input
                    type="checkbox"
                    checked={task.completed}
                    onChange={() => toggleTask(task.id, task.completed)}
                  />
                  <span className={task.completed ? 'completed' : ''}>
                    {task.title}
                  </span>
                  <span className="priority-badge">P{task.priority}</span>
                </div>
                <button
                  className="delete-btn"
                  onClick={() => deleteTask(task.id)}
                >
                  Delete
                </button>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  )
}

export default App