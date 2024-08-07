document.addEventListener('DOMContentLoaded', checkStatus);
        
function show(element) {
   var elem = document.getElementById(element);
    if (elem) {
        elem.style.display = 'flex';
    } else {
        console.error('Element with ID "' + elementId + '" not found');
    }
}

function hide(element) {
    var elem = document.getElementById(element);
      if (elem) {
          elem.style.display = 'none';
      } else {
          console.error('Element with ID "' + elementId + '" not found');
      }
}

function start(ref) {
    var delayValue;
    if(ref == 1){
        delayValue = document.getElementById('delayInput1').value;
    }
    else if(ref == 2){
        delayValue = document.getElementById('delayInput2').value;
    }
    else{
        delayValue = 1
    }


    fetch('/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ref: ref, delay: delayValue })
    })
    .then(response => response.json())
    .then(data => {
        updateStatus(data);
        console.log(data);
    });
}


function checkStatus() {
    fetch('/status')
        .then(response => response.json())
        .then(data => {
            updateStatus(data)
        })
        .catch(error => {
            console.error('Error checking status:', error);
            hideSwitching();
        });
}


function stop(ref) {
    fetch('/stop', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ref: ref })
    })
    .then(response => response.json())
    .then(data => {
        updateStatus(data)
    });
}

function updateStatus(data){
       
        if(data.ref1 == 'active'){
            hide('open1');
            show('active1');
            hide('close1')
        }
        else if (data.ref1 == 'open'){
            show('open1');
            hide('active1');
            hide('close1')
        }
        else if (data.ref1 == 'close'){
            hide('open1');
            hide('active1');
            show('close1')
        }

        if(data.ref2 == 'active'){
            hide('open2');
            show('active2');
            hide('close2')
        }
        else if (data.ref2 == 'open'){
            show('open2');
            hide('active2');
            hide('close2')
        }
        else if (data.ref2 == 'close'){
            hide('open2');
            hide('active2');
            show('close2')
        }
        
        var time1 = document.getElementById('time1');
        if (time1) {
            time1.innerText = data.ref1_time;
        } 
        
        var time2 = document.getElementById('time2');
        if (time2) {
            time2.innerText = data.ref2_time;
        } 

}