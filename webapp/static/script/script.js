$(document).ready(function() {
  if ($('#emailtable')) {
  var table = $('#emailtable').DataTable({
      
    info: true,
    ordering: true,
    paging: true,
    searching: true,
    
        "columns": [                //Read a DOM sourced table into data objects:
          { data: "id" },
          { data: "to" },
          { data: "from" },
          { data: "subject" },
          { data: "body",
          render: function (data, type, row) {     
            var color = 'black';
            if (data === 'Hello this is a test email') {
              color = '#62F5BC';
            }
            else if (data != 'a')
            color = '#f53d50';
            return '<span style="color:' + color + '">' + data + '</span>';
          } }
      ],

  
        
      


  });
}
} );




$(document).ready(function() {
  if ($('#logtable')) {
  var logtable = $('#logtable').DataTable({
      
    info: true,
    ordering: true,
    paging: true,
    searching: true,
    
        "columns": [                //Read a DOM sourced table into data objects:
          { data: "id" },
          { data: "date" },
          { data: "time" },
          { data: "to" },
          { data: "from" },
          { data: "subject" },
          { data: "message" },
          { data: "type" },         
          { data: "Action",
          render: function (data, type, row) { //Checks what value is in Action and Assigns colour
            var color = 'black';
            if (data === 'Allowed') {
              color = '#62F5BC';
            }
            else if (data != 'a')
            color = '#f53d50';
            return '<span style="color:' + color + '">' + data + '</span>';
          } }
      ],
  

  });
}
} );




//var $rows = $('#table tr');
//$('#searchInput').keyup(function() 
//{
//    var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();
//
//    $rows.show().filter(function() {
 //       var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
 //       return !~text.indexOf(val);
  //  }).hide();
//});