<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

if(!function_exists('getScheduleList'))
{
    function getScheduleList(){
        function timeCmp($a, $b) {
            if($a['weekday'] == $b['weekday']){

                $timeStrA = strtotime($a['time']);
                $timeStrB = strtotime($b['time']);
                if($timeStrA == $timeStrB){
                    return 0;
                }

                return ($timeStrA < $timeStrB) ? -1 : 1;
            }

            return ($a['weekday'] < $b['weekday']) ? -1 : 1;
        }

        $timeMapping = array(
            'SUN' => 0,
            'MON' => 1,
            'TUE' => 2,
            'WED' => 3,
            'THU' => 4,
            'FRI' => 5,
            'SAT' => 6
        );

        $scheduleTimes = ['TUE|12:00', 'WED|12:00'];
        $parsedTimeArr = array();
        foreach ($scheduleTimes as $key => $val) {
            $parsedTime = explode("|", $val);
            $weekday = $timeMapping[$parsedTime[0]];
            $time = $parsedTime[1];
            array_push($parsedTimeArr, array(
                'weekday'   => $weekday,
                'time'      => $time
            ));
        }

        uasort($parsedTimeArr, 'timeCmp');

        return $parsedTimeArr;
    }
}


if(!function_exists('getSiteTimezone')
{
    function getSiteTimezone()
    {
        return new DateTimeZone('Asia/Ho_Chi_Minh');
    }
}


function getScheduledTimeString() {

    $scheduledTimeArr = getScheduleList();
    $currTime = new DateTime();
    $currTime->setTimezone(getSiteTimezone());
    $currTimeStamp = $currTime->getTimestamp();
    $currWeekDay = date('w', $currTimeStamp);

    $currentWeekDay = date('w', $currTimeStamp);
    $scheduledTime = $currTime;
    for ($i=0; $i < count($scheduledTimeArr); $i++) {
        if($currentWeekDay <= $scheduledTimeArr[$i]['weekday']){
            if($currentWeekDay == $scheduledTimeArr[$i]['weekday']){
                $deltaTimeStr = strtotime($scheduledTimeArr[$i]['time']) - $currTimeStamp;
                if($deltaTimeStr > 300){
                    $scheduledTime->setTimestamp(strtotime($scheduledTimeArr[$i]['time']));
                    break;
                }
            }else{
                $scheduledTime->setTimestamp(strtotime($scheduledTimeArr[$i]['time']));
                $deltaDay = $scheduledTimeArr[$i]['weekday'] - $currWeekDay;
                $scheduledTime->add(new DateInterval('P'.(string) $deltaDay . 'D'));
                break;
            }
        }
    }
    if($scheduledTime == $currTime){
        $scheduledTime->setTimestamp(strtotime($scheduledTimeArr[0]['time']));
        $deltaDay = 7 - ($currWeekDay - $scheduledTimeArr[0]['weekday']);
        $scheduledTime->add(new DateInterval('P'.(string) $deltaDay . 'D'));
    }

    $expectedTimestring = $scheduledTime->getTimestamp();
    return $expectedTimestring;
}
