var dt = new Date();
function RenderDate()
{  
    document.getElementById("date_str").innerHTML = dt.toDateString();
    dt.setDate(1);
    var day = dt.getDay();
    var endDate = new Date(dt.getFullYear(),dt.getMonth() + 1,0).getDate();
    var prevDate = new Date(dt.getFullYear(),dt.getMonth(),0).getDate();
    var today1 = new Date();
    var months = ["January", 
       "February",
       "March",
       "April",
       "May", 
       "June", 
       "July", 
       "August",
       "September",
       "October", 
       "November", 
       "December"];
    
    document.getElementById("month").innerHTML = months[dt.getMonth()];
    
    var cells = "";
    
    for(x=day;x>0;x--)
    {
        cells+= "<div class='prev_date'>" +(prevDate-x+1)+ "</div>";
    }
    for(i=1; i<=endDate; i++)
    {
        if(i==today1.getDate() && dt.getMonth()==today1.getMonth())
        { cells+="<div class='today'>" + i + "</div>"; }
        else
        {
            cells+="<div>" + i + "</div>";
        }
    }    
    document.getElementsByClassName("days")[0].innerHTML =  cells;
}

function moveDate(para)
{
  if(para=='prev')
    {
    dt.setMonth(dt.getMonth()-1);
    }
  else if(para=='next')
    {
    dt.setMonth(dt.getMonth()+1);
    }
    RenderDate();
}