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

        $scheduleTimes = ['TUE|12:00', 'SAT|20:50'];
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

function getScheduledTimeString()
{

    $timeList       = getScheduleList();
    $currTime       = new DateTime();
    $currTimeStamp  = $currTime->getTimestamp();
    $currWeekDay    = date('w', $currTimeStamp);
    $scheduledTime  = $currTime;
    $isScheduled    = FALSE;

    for ($i=0; $i < count($timeList); $i++) {
        $weekday    = $timeList[$i]['weekday'];
        $time       = $timeList[$i]['time'];
        $deltaDay   = $weekday - $currWeekDay;
        $deltaTime  = strtotime($timeList[$i]['time']) - $currTimeStamp;

        if($deltaDay >= 0){
            $scheduledTime->setTimestamp(strtotime($timeList[$i]['time']));
            $scheduledTime->add(new DateInterval('P'.(string) $deltaDay . 'D'));
            $deltaTime = $scheduledTime->getTimestamp() - $currTimeStamp;

            if($deltaTime > 14400){
                $isScheduled = TRUE;
                break;
            }
        }
    }

    if(!$isScheduled){
        $deltaDay = 7 - ($currWeekDay - $timeList[0]['weekday']);
        $scheduledTime->setTimestamp(strtotime($timeList[0]['time']));
        $scheduledTime->add(new DateInterval('P'.(string) $deltaDay . 'D'));
    }

    return $scheduledTime->getTimestamp();
}
