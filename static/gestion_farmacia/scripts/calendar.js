document.addEventListener('DOMContentLoaded', function (){
    
    var calendarUI = document.getElementById('calendar')
    var calendar = new FullCalendar.Calendar(calendarUI, {
        timeZone: 'local',
        locale: 'es',
    });
    calendar.render();
});