#! /usr/local/bin/python3

attendees = ["ken", "Alena", "Treausre"]
attendees.append("ashley")
attendees.extend(["James", "Gill"])
optional_invitees = ["Ben.J", "Dave"]
potential_attendees = attendees + optional_invitees

print ("There are", len(potential_attendees), "potential attendees currently")
