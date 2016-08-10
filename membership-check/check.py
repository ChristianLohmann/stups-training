import requests
import click
import csv
from clickclick import Action, info


def shorten_email(email):
    tokenized = email.split('@')
    names = tokenized[0].split('.')
    return names[0][0] + ''.join(names[1:])


def fetch_mentoring_members(token):
    headers = {'Authorization': 'Bearer ' + token}
    r = requests.get('https://teams.auth.zalando.com/api/teams/mentoring', headers=headers)
    r.raise_for_status()
    data = r.json()
    members = data['member']
    return members


@click.command()
@click.option('--file', default='attendees.csv', type=click.Path())
@click.option('--token', type=click.STRING)
def main(file, token):
    with open(file) as peek:
        has_header = csv.Sniffer().has_header(peek.read(1024))
        peek.seek(0)  # rewind
        csv_file = csv.reader(peek, delimiter=',', quotechar='"')
        if has_header:
            next(csv_file)  # skip header row
        data = (str(row[0]) for row in csv_file)
        shortened = (shorten_email(email) for email in data)
        members = fetch_mentoring_members(token)
        print(', '.join(members))
        found = False
        non_mentoring_members = []
        for newbie in shortened:
            info('Checking newbie {}'.format(newbie))
            for member in members:
                if newbie.startswith(member):
                    found = True
                    break
            if not found:
                non_mentoring_members.append(newbie)
            else:
                found = False
        print('List of newbies not in mentoring team yet:')
        print('\n'.join(non_mentoring_members))

if __name__ == '__main__':
    main()
