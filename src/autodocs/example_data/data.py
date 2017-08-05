CSV1 = """policyID,statecode,county,eq_site_limit,hu_site_limit,fl_site_limit,fr_site_limit,tiv_2011,tiv_2012,eq_site_deductible,hu_site_deductible,fl_site_deductible,fr_site_deductible,point_latitude,point_longitude,line,construction,point_granularity
119736,FL,CLAY COUNTY,498960,498960,498960,498960,498960,792148.9,0,9979.2,0,0,30.102261,-81.711777,Residential,Masonry,1
448094,FL,CLAY COUNTY,1322376.3,1322376.3,1322376.3,1322376.3,1322376.3,1438163.57,0,0,0,0,30.063936,-81.707664,Residential,Masonry,3
206893,FLa,CLAY COUNTY,190724.4,190724.4,190724.4,190724.4,190724.4,192476.78,0,0,0,0,30.089579,-81.700455,Residential,Wood,1
333743,FL,CLAY COUNTY,0,79520.76,0,0,79520.76,86854.48,0,0,0,0,30.063236,-81.707703,Residential,Wood,3
172534,FLa,CLAY COUNTY,0,254281.5,0,254281.5,254281.5,246144.49,0,0,0,0,30.060614,-81.702675,Residential,Wood,1
785275,FL,CLAY COUNTY,0,515035.62,0,0,515035.62,884419.17,0,0,0,0,30.063236,-81.707703,Residential,Masonry,3
995932,FL,CLAY COUNTY,0,19260000,0,0,19260000,20610000,0,0,0,0,30.102226,-81.713882,Commercial,Reinforced Concrete,1
223488,FLa,CLAY COUNTY,328500,328500,328500,328500,328500,348374.25,0,16425,0,0,30.102217,-81.707146,Residential,Wood,1
433512,FL,CLAY COUNTY,315000,315000,315000,315000,315000,265821.57,0,15750,0,0,30.118774,-81.704613,Residential,Wood,1
142071,FL,CLAY COUNTY,705600,705600,705600,705600,705600,1010842.56,14112,35280,0,0,30.100628,-81.703751,Residential,Masonry,1
253816,FLa,CLAY COUNTY,831498.3,831498.3,831498.3,831498.3,831498.3,1117791.48,0,0,0,0,30.10216,-81.719444,Residential,Masonry,1
894922,FL,CLAY COUNTY,0,24059.09,0,0,24059.09,33952.19,0,0,0,0,30.095957,-81.695099,Residential,Wood,1
422834,FL,CLAY COUNTY,0,48115.94,0,0,48115.94,66755.39,0,0,0,0,30.100073,-81.739822,Residential,Wood,1
582721,FLa,CLAY COUNTY,0,28869.12,0,0,28869.12,42826.99,0,0,0,0,30.09248,-81.725167,Residential,Wood,1
842700,FL,CLAY COUNTY,0,56135.64,0,0,56135.64,50656.8,0,0,0,0,30.101356,-81.726248,Residential,Wood,1
874333,FL,CLAY COUNTY,0,48115.94,0,0,48115.94,67905.07,0,0,0,0,30.113743,-81.727463,Residential,Wood,1
580146,FL,CLAY COUNTY,0,48115.94,0,0,48115.94,66938.9,0,0,0,0,30.121655,-81.732391,Residential,Wood,3
456149,FL,CLAY COUNTY,0,80192.49,0,0,80192.49,86421.04,0,0,0,0,30.109537,-81.741661,Residential,Wood,1
767862,FL,CLAY COUNTY,0,48115.94,0,0,48115.94,73798.5,0,0,0,0,30.11824,-81.745335,Residential,Wood,3
353022,FL,CLAY COUNTY,0,60946.79,0,0,60946.79,62467.29,0,0,0,0,30.065799,-81.717416,Residential,Wood,1
367814,FLa,CLAY COUNTY,0,28869.12,0,0,28869.12,42727.74,0,0,0,0,30.082993,-81.710581,Residential,Wood,1"""

var = "(<equals:1:FL>&&<endswith:2:NTY>)||<row:*3>"

JSON1 = {
	"employees": [{
			"employee": {
				"first": "Matt",
				"last": "Wyrick",
				"from": {
					"city": "Franklin",
					"state": "Indiana"
				},
				"age": 21,
				"activities": [{
						"activity": "Riding Bikes",
						"proficiency": "Good"
					},
					{
						"activity": "Cooking",
						"proficiency": "Great"
					},
					{
						"activity": "Singing",
						"proficiency": "Bad"
					}
				]
			}
		},

		{
			"employee": {
				"first": "Eric",
				"last": "Jones",
				"from": {
					"city": "Madison",
					"state": "Indiana"
				},
				"age": 73,
				"activities": [{
						"activity": "Chess",
						"proficiency": "Great"
					},
					{
						"activity": "Guitar",
						"proficiency": "Okay"
					}
				]
			}
		},
		{
			"employee": {
				"first": "Greg",
				"last": "Lang",
				"from": {
					"city": "Kansas City",
					"state": "Kansas"
				},
				"age": 63,
				"activities": [{
						"activity": "Writing",
						"proficiency": "Very Good"
					},
					{
						"activity": "Netflix",
						"proficiency": "Great"
					}
				]
			}
		},
		{
			"employee": {
				"first": "Brian",
				"last": "Adams",
				"from": {
					"city": "Washington",
					"state": "DC"
				},
				"age": 35
			}
		}
	]

}


JSON2 = {
        "events": [{
            "date": "-300",
            "description": "Pilgrims travel to the healing temples of Asclepieion to be cured of their ills. After a ritual purification the followers bring offerings or sacrifices.",
            "lang": "en",
            "category1": "By place",
            "category2": "Greece",
            "granularity": "year"
        },
            {
                "date": "-300",
                "description": "Pyrrhus, the King of Epirus, is taken as a hostage to Egypt after the Battle of Ipsus and makes a diplomatic marriage with the princess Antigone, daughter of Ptolemy and Berenice.",
                "lang": "en",
                "category1": "By place",
                "category2": "Egypt",
                "granularity": "year"
            },
            {
                "date": "-300",
                "description": "Ptolemy concludes an alliance with King Lysimachus of Thrace and gives him his daughter Arsinoe II in marriage.",
                "lang": "en",
                "category1": "By place",
                "category2": "Egypt",
                "granularity": "year"
            },
            {
                "date": "-300",
                "description": "Seleucus founds the city of Antioch, some 20 miles up the Orontes River, naming it after his father.",
                "lang": "en",
                "category1": "By place",
                "category2": "Seleucid Empire",
                "granularity": "year"
            },
            {
                "date": "-300",
                "description": "After the death of his wife Apama, Seleucus marries Stratonice, daughter of Demetrius Poliorcetes.",
                "lang": "en",
                "category1": "By place",
                "category2": "Seleucid Empire",
                "granularity": "year"
            },
            {
                "date": "-300",
                "description": "The central texts of Jainism, the Jain scriptures, are recorded (approximate date).{{Citation needed|date=March 2009}}",
                "lang": "en",
                "category1": "By place",
                "category2": "India",
                "granularity": "year"
            },
            {
                "date": "-300",
                "description": "In Pella (in Macedonia), the artist Gnosis makes a mosaic floor decoration called ''Stag Hunt'' and even signs it with ampquotGnosis made itampquot. It is today preserved at the Archaeological museum in Pella.",
                "lang": "en",
                "category1": "By topic",
                "category2": "Art",
                "granularity": "year"
            },
            {
                "date": "-299",
                "description": "The Samnites, seizing their chance when Rome is engaged on the Lombard plain, start the third Samnite War with a collection of mercenaries from Gaul, Sabine, and Etruscan allies to help them.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-299",
                "description": "The state of Qin attacks eight cities of the state of Chu. Chu then sends an envoy to ask the King of Huai to go to Qin to negotiate peace. Qu Yuan risks his life to go up to the court to persuade the King of Huai not to go to the negotiation.",
                "lang": "en",
                "category1": "By place",
                "category2": "China",
                "granularity": "year"
            },
            {
                "date": "-299",
                "description": "King Wuling of Zhao abdicates the throne of Zhao to his son.",
                "lang": "en",
                "category1": "By place",
                "category2": "China",
                "granularity": "year"
            },
            {
                "date": "-298",
                "description": "The Samnites defeat the Romans under Lucius Cornelius Scipio Barbatus in the Battle of Camerinum, first battle of the Third Samnite War.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-298",
                "description": "The Roman armies penetrate into the heart of the Samnite territory and then capture the Samnite cities of Taurasia, Bovianum Vetus and Aufidena.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-298",
                "description": "Agathocles, king of Syracuse, assists the Italian Greeks against the Bruttians and supported the Greeks against the Romans.",
                "lang": "en",
                "category1": "By place",
                "category2": "Sicily",
                "granularity": "year"
            },
            {
                "date": "-298",
                "description": "Ptolemy gives his stepdaughter Theoxena in marriage to Agathocles, the tyrant of Syracuse (in south-eastern Sicily).",
                "lang": "en",
                "category1": "By place",
                "category2": "Egypt",
                "granularity": "year"
            },
            {
                "date": "-298",
                "description": "Ptolemy finally brings the rebellious region of Cyrene under his control. He places the region under the rule of his stepson Magas.",
                "lang": "en",
                "category1": "By place",
                "category2": "Egypt",
                "granularity": "year"
            },
            {
                "date": "-298",
                "description": "Bindusara succeeds his father Chandragupta Maurya as emperor of the Mauryan Empire.",
                "lang": "en",
                "category1": "By place",
                "category2": "India",
                "granularity": "year"
            },
            {
                "date": "-297",
                "description": "Fabius Maximus Rullianus becomes consul for the fourth time. He defeats the Samnites in a battle near Tifernum.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-297",
                "description": "Following Cassander's death from illness, Philip IV, Cassander's eldest son, succeeds his father as King of Macedon, but soon after coming to the throne suffers from a wasting disease and dies. Antipater, the next son, rules jointly with his brother Alexander V.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-297",
                "description": "Demetrius Poliorcetes returns to Greece with the aim of becoming master of Macedonia. While Demetrius is in Greece, Lysimachus seizes his possessions in Asia Minor.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-297",
                "description": "Ptolemy decides to support Pyrrhus of Epirus and restores him to his kingdom. At first Pyrrhus reigns with a kinsman, Neoptolemus II of Epirus (who is a son of Cleopatra of Macedonia and a nephew of Alexander the Great), but soon he has him assassinated.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-297",
                "description": "Chandragupta Maurya goes to Sravana Belagola near Mysore to live in the way of Jains.",
                "lang": "en",
                "category1": "By place",
                "category2": "India",
                "granularity": "year"
            },
            {
                "date": "-297",
                "description": "Bindusara his son ascends to the Pataliputra throne.",
                "lang": "en",
                "category1": "By place",
                "category2": "India",
                "granularity": "year"
            },
            {
                "date": "-296",
                "description": "Ptolemy makes peace with Demetrius Poliorcetes, to whom he betrothes his daughter Ptolemais.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-296",
                "description": "The temple to Bellona is erected at the south end of the prata Flaminia, later the Circus Flaminius, in Rome.ampampPlatner and Ashby, ''A Topographical Dictionary of Rome''. Oxford University Press, 1926. p. 82.ampamp",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-295",
                "description": "The Battle of Sentinum west of Anconum ends in defeat for a formidable coalition of Samnites, Etruscans, Umbrians, and their Gallic allies at the hands of the Roman legions commanded by consuls Publius Decius Mus (who is killed in the battle) and Quintus Fabius Maximus Rullianus. The Romans lose nearly 8,000 men but kill some 25,000 of the enemy and force peace on the Etruscans.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-295",
                "description": "Athens falls to Demetrius Poliorcetes after a bitter siege, and its tyrant Lachares is killed.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-295",
                "description": "The King of Macedon, Antipater II, murders his mother Thessalonica, accusing her of being too fond of his brother and co-ruler Alexander V.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-294",
                "description": "Archidamus IV, king of Sparta, son of Eudamidas I and grandson of Archidamus III, is defeated by Demetrius Poliorcetes of Macedonia in a battle at Mantinea. Sparta is saved only because Demetrius is called away by the threatening activities of his rivals Lysimachus and Ptolemy.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-294",
                "description": "Alexander V of Macedon is ousted by his brother, Antipater II. Therefore Alexander V turns to Demetrius Poliorcetes for help in recovering his throne. However, Demetrius Poliorcetes establishes himself on the throne of Macedonia and then murders Alexander V. Antipater II loses the throne of Macedonia but is able to survive.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-294",
                "description": "Pyrrhus of Epirus exploits the dynastic quarrel in Macedonia involving Alexander V of Macedon, his brother, Antipater II and Demetrius Poliorcetes to take over the frontier areas of Parauaea and Tymphaea, along with Acarnania, Ampholochia, and Ambracia.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-294",
                "description": "Lysimachus concludes a peace with Demetrius Poliorcetes whereby Demetrius Poliorcetes is recognized as ruler of Macedonia.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-294",
                "description": "Ptolemy gains control over Cyprus and the Phoenician coastal towns of Tyre and Sidon.",
                "lang": "en",
                "category1": "By place",
                "category2": "Egypt",
                "granularity": "year"
            },
            {
                "date": "-294",
                "description": "Stratonice, daughter of Demetrius Poliorcetes and wife of Seleucus marries her stepson Antiochus. Seleucus has reportedly instigated the marriage after discovering that his son by his late wife Apama was in danger of dying of lovesickness as he has fallen in love with his beautiful stepmother.",
                "lang": "en",
                "category1": "By place",
                "category2": "Seleucid Empire",
                "granularity": "year"
            },
            {
                "date": "-293",
                "description": "The Battle of Aquilonia is  fought between the Roman Republic and the Samnites, near the current city of Aquilonia in Campania (in southern Italy). The Romans, led by the consuls Lucius Papirius Cursor and Spurius Carvilius Maximus, are victorious. After the battle, the Samnites flee into the city of Aquilonia and into their camp. The camp is captured and looted by the Romans, while the city is eventually taken, with many of the Samnite survivors being slaughtered in the fighting.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-293",
                "description": "Rome suffers from the plague. The worship of Aesculapius is introduced from Epidaurus to Rome in the hope of averting the plague.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-293",
                "description": "When an invasion of nomads threatens the eastern possessions of his realm (i.e. between the Caspian Sea and the Aral Sea and the Indian Ocean), Seleucus hands over the government of these lands west of the Euphrates to his son Antiochus. Antiochus is appointed co-regent and commander-in-chief of these territories.",
                "lang": "en",
                "category1": "By place",
                "category2": "Persia",
                "granularity": "year"
            },
            {
                "date": "-293",
                "description": "The State of Qin, led by commander Bai Qi, wins a decisive victory over the States of Wei and Han in the Battle of Yique. As part of the terms of defeat, Han and Wei are forced to concede land to Qin.",
                "lang": "en",
                "category1": "By place",
                "category2": "China",
                "granularity": "year"
            },
            {
                "date": "-292",
                "description": "Lysimachus tries to extend his influence beyond the Danube River, but he is defeated and taken prisoner by the Getae (Dacian) king Dromichaetes (Dromihete). Eventually, Lysimachus is set free and a peace is agreed between the Getae and Lysimachus. This peace agreement is strengthened further by the marriage of Dromichaetes with Lysimachus' daughter.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-292",
                "description": "While Demetrius Poliorcetes is campaigning in Boeotia, he receives news that Lysimachus, the ruler of Thrace, has been taken prisoner by Dromichaetes. Hoping to seize Lysimachus's territories in Thrace, Demetrius, delegates command of his forces in Boeotia to his son, Antigonus and immediately marches north. However, while he is away, the Boeotians rise in rebellion, but are defeated by Antigonus, who bottles them up in the city of Thebes.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-291",
                "description": "Demetrius Poliorcetes joins his son, Antigonus, in the siege of Thebes. As the Thebans defend their city stubbornly, Demetrius forces his men to attack the city at great cost. Demetrius finally takes the city after using siege engines to demolish its walls.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-291",
                "description": "The Romans storm and take the Samnite city of Venusia.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-290",
                "description": "Roman general and consul, Manius Curius Dentatus, gains a decisive victory over the Samnites, thereby ending a war that has lasted 50 years. He also reduces the Sabine insurgents to submission, their territory is annexed and they are granted civitas sine suffragio (ampquotcitizenship without the right to voteampquot). The Samnites are recognised by the Romans as autonomous allies. The Samnites are forced to give up some of their land to the Romans as compensation.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-290",
                "description": "Berenice, wife of Ptolemy, is proclaimed queen of Egypt. Ptolemy has the city of Berenice built on the Red Sea in her honour. It becomes a great emporium for Egyptian trade with the East.",
                "lang": "en",
                "category1": "By place",
                "category2": "Egypt",
                "granularity": "year"
            },
            {
                "date": "-289",
                "description": "The tyrant of Syracuse, Agathocles, dies after restoring the Syracusan democracy on his death bed, by stating that he does not want his sons to succeed him as king. However, the resulting dissension among his family about the succession leads to a renewal of Carthaginian power in Sicily.",
                "lang": "en",
                "category1": "By place",
                "category2": "Sicily",
                "granularity": "year"
            },
            {
                "date": "-288",
                "description": "The Macedonian King, Demetrius Poliorcetes, faces a combined attack from Lysimachus and Phyrrhus, king of Epirus, after Seleucus, Ptolemy and Lysimachus form a coalition to block plans by Demetrius to invade Asia Minor. Ptolemy's fleet appears off Greece, inciting the cities to revolt.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-288",
                "description": "Athens revolts and Demetrius besieges the city. Pyrrhus takes Thessaly and the western half of Macedonia and, with the assistance of Ptolemy's fleet, relieves Athens from Demetrius' siege.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-288",
                "description": "After the Egyptian fleet participates decisively in the liberation of Athens from Macedonian occupation, Ptolemy obtains the protectorate over the League of Islanders, which includes most of the Greek islands in the Aegean Sea. Egypt's maritime supremacy in the Mediterranean in the ensuing decades is based on this alliance.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-288",
                "description": "Following the death of Agathocles, some of his disbanded mercenaries seize Messana in northeast Sicily and set up a society, calling themselves Mamertines (Sons of Mars). The city becomes a base from which they will ravage the Sicilian countryside.",
                "lang": "en",
                "category1": "By place",
                "category2": "Sicily",
                "granularity": "year"
            },
            {
                "date": "-288",
                "description": "The Sri Maha Bodhi Sacred Fig tree is planted at Anuradhapura, Sri Lanka. This is the earliest known planting date for any planted tree still surviving.",
                "lang": "en",
                "category1": "By place",
                "category2": "Sri Lanka",
                "granularity": "year"
            },
            {
                "date": "-287",
                "description": "A new law, Lex Hortensia, gives much greater power to the plebeian Assembly compared to the Senate. This law is passed following a threat from plebeian soldiers to secede. In the face of this threat, the Senate yields to plebeian concerns over their lack of political power and over their level of debt to the aristocracy. The law is named after Quintus Hortensius, a plebeian, who is made dictator to settle the controversy.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-287",
                "description": "With the Lex Hortensia in place, in theory the political distinctions in Rome between the patricians and the plebeians disappear. However, in practice, the coalition of leading plebeian families keep control which means that the patricians are able to largely nullify the power of the assemblies. So Roman government continues to be oligarchic in character.",
                "lang": "en",
                "category1": "By place",
                "category2": "Roman Republic",
                "granularity": "year"
            },
            {
                "date": "-287",
                "description": "The Macedonians resent the extravagance and arrogance of Demetrius Poliorcetes and are not prepared to fight a difficult campaign for him. When Pyrrhus of Epirus takes the Macedonian city of Verroia, Demetrius' army promptly deserts and goes over to Pyrrhus' side as he is much admired by the Macedonians for his bravery. At this change of fortune, Phila, the mother of Antigonus, kills herself with poison.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-287",
                "description": "Demetrius decides to leave Antigonus in charge of the war in Greece, assembles all his ships and embarks with his troops to attack Caria and Lydia, provinces in Asia Minor controlled by Lysimachus.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-287",
                "description": "Agathocles is sent by his father Lysimachus against Demetrius. Agathocles defeats Demetrius and drives him out of his father's provinces.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            },
            {
                "date": "-287",
                "description": "Pyrrhus is proclaimed King of Macedonia.",
                "lang": "en",
                "category1": "By place",
                "category2": "Greece",
                "granularity": "year"
            }
        ]
    }




