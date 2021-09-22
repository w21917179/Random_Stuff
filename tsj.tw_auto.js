function autoUpgrade() {
    var tech = document.getElementsByClassName('col-12 text-center mt-2')[1].innerText.match(/\d+[.]?\d*(e\+)?\d*/g)[1];
    var potato = document.getElementsByClassName('table table-striped table-hover')[0].innerText.match(/\d+[.]?\d*(e\+)?\d*/g)[1];
    var plane = document.getElementsByClassName('table table-striped table-hover')[0].innerText.match(/\d+[.]?\d*(e\+)?\d*/g)[3];
    
    var tech_digi = Number(tech.substring(0,4));
    var tech_e = Number(tech.substring(6));
    var potato_digi = Number(potato.substring(0,4));
    var potato_e = Number(potato.substring(6));
    var plane_digi = Number(plane.substring(0,4));
    var plane_e = Number(plane.substring(6));
  
    console.log("tech_e: " + tech_e);
    console.log("potato_e: " + potato_e);
    console.log("plane_e: " + plane_e);

    if( Number(tech) > Number(potato) || tech_e > potato_e || (tech_e == potato_e && tech_digi > potato_digi)){
      document.getElementsByClassName('btn btn-primary btn-sm')[0].click();
      console.log("升級薯餅!");
    }
    else if ( Number(tech) > Number(plane) || tech_e > plane_e || (tech_e == plane_e && tech_digi > plane_digi)){
      document.getElementsByClassName('btn btn-primary btn-sm')[1].click();
      console.log("升級飛機杯!");
    }
  }
  
  var intervalID = setInterval(autoUpgrade, 1000);