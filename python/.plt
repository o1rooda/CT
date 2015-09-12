@startuml
start
:get user input F or C;
:get user input temperature;
if (user input F) then (F)
    :convert F to C;
elseif(user input C) then(C)
    :convert C to F;
else(neither F nor C)
:print "user input error";
endif
:print result;
stop
@enduml