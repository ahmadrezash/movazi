;var bar=new ProgressBar.Circle(circle,{color:'#000000',strokeWidth:6,value:0.6,trailWidth:1,easing:'easeInOut',duration:1400,text:{autoStyleContainer:false},from:{color:'#00b0bd',width:1},to:{color:'#00b0bd',width:6},step:function(state,circle){circle.path.setAttribute('stroke',state.color);circle.path.setAttribute('stroke-width',state.width);var value=Math.round((circle.value()*20).toString());if(value===0){circle.setText('');}else{circle.setText('<i class="fas fa-book-open fa-1x color" style="color:white "></i>'+value);}}});bar.text.style.fontSize='2rem';bar.animate(1.0)
var bar=new ProgressBar.Circle(circle2,{color:'#000000',strokeWidth:6,value:0.6,trailWidth:1,easing:'easeInOut',duration:1400,text:{autoStyleContainer:false},from:{color:'#00b0bd',width:1},to:{color:'#00b0bd',width:6},step:function(state,circle){circle.path.setAttribute('stroke',state.color);circle.path.setAttribute('stroke-width',state.width);var value=Math.round((circle.value()*20).toString());if(value===0){circle.setText('');}else{circle.setText('<i class="fas fa-chalkboard-teacher fa-1x color" style="color:white"></i>'+value);}}});bar.text.style.fontSize='2rem';bar.animate(1.0)
var bar=new ProgressBar.Circle(circle3,{color:'#000000',strokeWidth:6,value:0.6,trailWidth:1,easing:'easeInOut',duration:1400,text:{autoStyleContainer:false},from:{color:'#00b0bd',width:1},to:{color:'#00b0bd',width:6},step:function(state,circle){circle.path.setAttribute('stroke',state.color);circle.path.setAttribute('stroke-width',state.width);var value=Math.round((circle.value()*4).toString());if(value===0){circle.setText('');}else{circle.setText('<i class="fas fa-handshake fa-1x" style="color:white"></i>'+value);}}});bar.text.style.fontSize='2rem';bar.animate(1.0)
var bar=new ProgressBar.Circle(circle4,{color:'#000000',strokeWidth:6,value:0.6,trailWidth:1,easing:'easeInOut',duration:1400,text:{autoStyleContainer:false},from:{color:'#00b0bd',width:1},to:{color:'#00b0bd',width:6},step:function(state,circle){circle.path.setAttribute('stroke',state.color);circle.path.setAttribute('stroke-width',state.width);var value=Math.round((circle.value()*24).toString());if(value===0){circle.setText('');}else{circle.setText('<i class="fas fa-video fa-1x" style="color:white"></i>'+value);}}});bar.text.style.fontSize='2rem';bar.animate(1.0)