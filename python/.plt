@startuml

start

:sum=0;
repeat
    if (num is not divided by 3 or 5) then (true)
    :add num to sum;
    endif
repeat while (num is 1000?)
:print sum;

stop

@enduml