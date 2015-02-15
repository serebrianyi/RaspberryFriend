from util.DateUtil import DateUtil
import requests


class TramHandler(object):

    def process(self, address_from, address_to, waypoint):

        #get first part of route: src -> waypoint
        response_before = self._get_response(address_from, waypoint, str(int(self._get_current_time())))
        departure_time_text = response_before["routes"][0]["legs"][0]["departure_time"]["text"]
        arrival_time_value = response_before["routes"][0]["legs"][0]["departure_time"]["value"]

        #get second part of route: waypoint -> dest
        response_after = self._get_response(waypoint, address_to, str(arrival_time_value))
        departure_time_after_value = response_after["routes"][0]["legs"][0]["departure_time"]["value"]

        #calculate waiting time by tram change
        waiting_time = str(int((int(departure_time_after_value)-int(arrival_time_value))/60))

        return "Leave at %s (%s - wait for %s min)" % (
            departure_time_text,
            (",".join(self._get_switches(response_after, response_before))),
            waiting_time)

    def _get_current_time(self):
        return DateUtil.get_current_time()

    def _get_response(self, src, dest, time):
        url = "http://maps.googleapis.com/maps/api/directions/json?origin=" + src + "&destination=" + dest + "&departure_time=" + time + "&mode=transit&units=metric"
        r = requests.get(url)
        return r.json()

    def _get_lines(self, step):
        if "transit_details" in step:
            return step["transit_details"]["line"]["short_name"]
        else:
            return None

    def _get_switches(self, response_after, response_before):
        switches_before = list(map(lambda x: self._get_lines(x), response_before["routes"][0]["legs"][0]["steps"]))
        switches_after = list(map(lambda x: self._get_lines(x), response_after["routes"][0]["legs"][0]["steps"]))
        switches = list(filter(lambda x: x is not None, switches_before + switches_after))
        return switches

