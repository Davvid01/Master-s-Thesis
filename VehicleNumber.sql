Select VehicleNumber, count(*) as Liczba
from BussesTrams
group by VehicleNumber
having COUNT(*)=1
/*order by Lines, Time DESC*/
