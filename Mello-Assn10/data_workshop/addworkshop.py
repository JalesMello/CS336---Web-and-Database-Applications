from registration.models import Workshop


session1a = Workshop(
    title = "Client Procedures, Etiquette, and Legal",
    session = "Session 1",
    room = "Room 1A",
    start = "9:00 am",
    end = "11:30 am",
)
session1a.save()

session1b = Workshop(
    title = "Contract and Relationship Building",
    session = "Session 1",
    room = "Room 1B",
    start = "12:30 pm",
    end = "3:00 pm",
)
session1b.save()

session1c = Workshop(
    title = "Closing Techniques",
    session = "Session 1",
    room = "Room 1C",
    start = "4:00 pm",
    end = "6:30 pm",
)
session1c.save()

session2a = Workshop(
    title = "Accounting Procedures",
    session = "Session 2",
    room = "Room 1B",
    start = "9:00 am",
    end = "11:30 am",
)
session2a.save()

session2b = Workshop(
    title = "H.R. Procedures",
    session = "Session 2",
    room = "Room 1C",
    start = "12:30 pm",
    end = "3:00 pm",
)
session2b.save()

session2c = Workshop(
    title = "Legal and Taxes",
    session = "Session 2",
    room = "Room 1A",
    start = "4:00 pm",
    end = "6:30 pm",
)
session2c.save()

session3a = Workshop(
    title = "Production Procedures",
    session = "Session 3",
    room = "Room 1C",
    start = "9:00 am",
    end = "11:30 am",
)
session3a.save()

session3b = Workshop(
    title = "Purchasing Procedures",
    session = "Session 3",
    room = "Room 1A",
    start = "12:30 pm",
    end = "3:00 pm",
)
session3b.save()

session3c = Workshop(
    title = "Project and Timeline Coordination",
    session = "Session 3",
    room = "Room 1B",
    start = "4:00 pm",
    end = "6:30 pm",
)
session3c.save()
