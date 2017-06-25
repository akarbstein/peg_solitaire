FROM akarbstein/peg_solitaire_live
LABEL maintainer "alexander.karbstein@gmail.com"

ADD tests /peg_solitaire/tests
RUN mkdir /coverage_report
RUN pip install coverage
WORKDIR /peg_solitaire
CMD ["bash"]