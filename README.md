# cs1.1-oop-design-challenge

Socialorm is an idea I just got to recognise a few months ago. It instigates social interaction within student dorms. Each student will have a profile along with a status and event attendance for other students to know about and join in. Dorms are usually buildings within the city that is governed by the education institution.

An institution has 1 more residences, and in each residence there are floors, and in each floor there are students. Students then can attend events that the event organiser (who is also a student) has created.

The main challenge in this project was the permissions. The EventOrganiser Class acts as a subclass to Student but it invokes methods indirectly via Event Class. This is so that event class cannot be altered except by the EventOrganiser.

Other than that, all of classes are components of another class.