g.db = connect_db()
cursor = g.db.execute(
  'select name, due_date, priority, task_id from tasks where status=1'
)
open_tasks = [
    dict(name=row[0], due_date=row[1], priority=row[2],
      task_id=row[3]) for row in cursor.fetchall()
]
cursor = g.db.execute(
  'select name, due_date, priority, task_id from tasks where status=0'
  )
closed_tasks = [
    dict(name=row[0], due_date=row[1], priority=row[2],
      task_id=row[3]) for row in cursor.fetchall()
]
g.db.close()
return render_template(
    'tasks.html',
    form=AddTaskForm(request.form),
    open_tasks=open_tasks,
    closed_tasks=closed_tasks
  )

  # from  new_task
  g.db = connect_db()
name = request.form['name']
date = request.form['due_date']
priority = request.form['priority']
if not name or not date or not priority:
  flash("All fields are required. Please try again.")
  return redirect(url_for('tasks'))
else:
  g.db.execute('insert into tasks (name, due_date, priority, status) \
  values (?, ?, ?, 1)',  [
  request.form['name'],
  request.form['due_date'],
  request.form['priority']
  ]
)
g.db.commit()
g.db.close()
flash('New entry has been successfully posted. Thanks.')
return redirect(url_for('tasks'))

# from /complete
   g.db = connect_db()
    g.db.execute(
    	'update tasks set status = 0 where task_id='+str(task_id)
    )
    g.db.commit()
    g.db.close()
    flash("The task was marked as complete.")
    return redirect(url_for('tasks'))

# from /delete
g.db = connect_db()
	g.db.execute('delete from tasks where task_id=' + str(task_id))
	g.db.commit()
	g.db.close()
	flash('the task has been deleted.')
	return redirect(url_for('tasks'))

    
