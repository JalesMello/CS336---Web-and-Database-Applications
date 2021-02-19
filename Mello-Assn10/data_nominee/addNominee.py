from awardnominee.models import AwardNominee


person1 = AwardNominee(
    name = "Bill Jefferson",
    description = "Bill Jefferson works in Accounting",
    image = "bill_jefferson.png",
    votes = 0,
)
person1.save()


person2 = AwardNominee(
    name = "Christina Johnson",
    description = "Christina Johnson works in Sales",
    image = "christina_johnson.png",
    votes = 0,
)
person2.save()


person3 = AwardNominee(
    name = "Jake Phillips",
    description = "Jake Phillips works in Project/Production Coordination",
    image = "jake_phillips.png",
    votes = 0,
)
person3.save()