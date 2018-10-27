
$('th').click(function(){
    var table = $(this).parents('table').eq(0)
    var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()))
    this.asc = !this.asc
    if (!this.asc){rows = rows.reverse()}
    for (var i = 0; i < rows.length; i++){table.append(rows[i])}
})
function comparer(index) {
    return function(a, b) {
        var valA = getCellValue(a, index), valB = getCellValue(b, index)
        return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.toString().localeCompare(valB)
    }
}
function getCellValue(row, index){ return $(row).children('td').eq(index).text() }



(function() {
  // Get all the toggletip buttons
  var toggletips = document.querySelectorAll('[data-toggletip-content]');

  // Iterate over them
  Array.prototype.forEach.call(toggletips, function (toggletip) {
    // Get the message from the data-content element
    var message = toggletip.getAttribute('data-toggletip-content');

    // Get the live region element
    var liveRegion = toggletip.nextElementSibling;

    // Toggle the message
    toggletip.addEventListener('click', function () {
        liveRegion.innerHTML = '';
        window.setTimeout(function() {
          liveRegion.innerHTML = '<span class="toggletip-bubble">'+ message +'</span>';
        }, 100);
    });

    // Close on outside click
    document.addEventListener('click', function (e) {
      if (toggletip !== e.target) {
        liveRegion.innerHTML = '';
      }                        
    });

    // Remove toggletip on ESC
    toggletip.addEventListener('keydown', function(e) {
      if ((e.keyCode || e.which) === 27)
      liveRegion.innerHTML = '';
    });
  });
}());           