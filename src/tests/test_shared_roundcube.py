from ..core.shared.roundcube.roundcube import RoundcubeMock

def test_get_last_received_email():
    roundcube_mock = RoundcubeMock()
    assert roundcube_mock.getLastReceivedEmail() == "Hallo liebe Studierende, ich hoffe ihr habt alle die Aufgabe 1.1 erfolgreich abgegeben. Falls nicht, dann wird es höchste Zeit. Ich wünsche euch noch einen schönen Tag. Viele Grüße, euer Professor Karsten"
