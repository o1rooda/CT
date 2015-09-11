@startuml
start
:get user input1;
:get user input2;
if (1==2) then (1==2)
    :print "draw";
elseif(1=='scissor')
    if (2=='rock')
        :print "rock wins";
    elseif(2=='paper')
        :print "scissor wins";
    endif
elseif(1=='rock')
    if (2=='scissor')
        :print "rock wins";
    elseif(2=='paper')
        :print "paper wins";
    endif
elseif(1=='paper')
    if (2=='scissor')
        :print "scissor wins";
    elseif(2=='rock')
        :print "paper wins";
    endif
else
    :print "error";
endif
:print result;
stop
@enduml