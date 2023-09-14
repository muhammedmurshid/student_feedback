odoo.define('student_feedback.custom_widget', function (require) {
    'use strict';
    console.log('cop')
      var clipboard = new ClipboardJS('.your-copy-button', {
        text: function () {
            // Return the text you want to copy to the clipboard
            console.log('cop1')
            return 'Text to be copied';
        }
    });

    clipboard.on('success', function (e) {
        console.log('cop2')
        // Display a success message or perform other actions
        alert('Text copied to clipboard: ' + e.text);
    });
});