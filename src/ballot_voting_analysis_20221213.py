# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:42:04 2022

@author: awby
"""

from pandas import read_csv, cut
members = read_csv('data/members/members_20221207.csv', encoding='latin')

ballot = read_csv('data/members/ballot_2022/pay_ballot_members_20221212.csv')

schools = members.groupby('Workplace Code').agg({'Membership Number ': 'count'})
schools['Members'] = cut(
    schools['Membership Number '],
    [0, 5, 10, 20, 40, 80, 500],
    labels = [
        '1 to 4',
        '5 to 9',
        '10 to 19',
        '20 to 39',
        '40 to 79',
        '80+'
        ]
    )


b2 = ballot.merge(
    members[
        [
            'Membership Number ', 
            'Phase Of Edu Desc',
            'Age ',
            'Gender ',
            ]
        ], 
    how='left', 
    left_on='membership_number', 
    right_on='Membership Number '
    ).merge(
        schools['Members'],
        how='left',
        left_on='workplace_code',
        right_index=True
        )

b2.loc[b2.confirmed_vote=='Yes', 'voted']=1
b2.loc[(b2.confirmed_vote!='Yes')|(b2.confirmed_vote.isnull()), 'voted']=0
b2.loc[b2.ballot_replacement_requested=='Yes', 'new_ballot_requested']=1
b2.loc[(b2.ballot_replacement_requested!='Yes')|(b2.ballot_replacement_requested.isnull()), 'new_ballot_requested']=0

#b2.groupby('Phase Of Edu Desc').agg({'voted': 'sum', 'membership_number': 'count'}).to_csv('voted by phase.csv')

b2.groupby(
    ['Phase Of Edu Desc', 'Gender ']
    ).agg(
        {'voted': 'sum', 'membership_number': 'count'}
        ).unstack().to_csv('voted by phase and sex.csv')

b2.groupby(
    ['Phase Of Edu Desc', 'Members', 'Gender ']
    ).agg(
        {'voted': 'sum', 'membership_number': 'count'}
        ).unstack().to_csv('voted by phase, members and sex.csv')

b2.groupby(
    ['Members', 'Gender ']
    ).agg(
        {'voted': 'sum', 'membership_number': 'count'}
        ).unstack().to_csv('voted by members and sex.csv')

b2.groupby(
    ['Members']
    ).agg(
        {'voted': 'sum', 'membership_number': 'count'}
        ).to_csv('voted by members.csv')

b2.groupby('Phase Of Edu Desc').agg({'voted': 'sum', 'membership_number': 'count', 'new_ballot_requested':'sum' }).to_csv('voted and new ballotby phase.csv')