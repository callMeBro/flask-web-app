function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ noteId: noteId })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to delete note');
        }
        return response.json();
    })
    .then(data => {
        // Handle success response
        
        if (data.reload === true) {
            location.reload(); // Reload the page
           
        }
    })
    .catch(error => {
        console.error('Error deleting note:', error);
    });
    
}
